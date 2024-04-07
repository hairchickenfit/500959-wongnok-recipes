from django.contrib import messages
from django.shortcuts import redirect, render, reverse

import datetime
import zoneinfo

from . import models as recipe_models


def all_recipe(request):
    context = {}
    wongnok_recipe_objs = recipe_models.WongnokRecipe.objects.all()
    all_recipe_objs = []
    for obj in wongnok_recipe_objs:
        _rating_log_objs = recipe_models.RatingLog.objects.filter(rated_recipe=obj.auto_id)
        ratings = [float(item.rating) for item in _rating_log_objs]
        rating = '%.2f' % float(sum(ratings) / len(ratings)) if len(ratings) != 0 else '0.00'
        all_recipe_objs.append(
            [
                obj.auto_id,
                obj.title,
                obj.duration,
                obj.cooking_level,
                obj.owner.first_name + ' ' + obj.owner.last_name,
                rating
            ]
        )    
    context['all_recipe_objs'] = all_recipe_objs
    return render(request, 'recipe/all_recipe.html', context)

def view_recipe(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            recipe_id = request.GET.get('recipeID', None)
            rating = request.GET.get('rating', None)
            wongnok_recipe_obj = recipe_models.WongnokRecipe.objects.get(auto_id=recipe_id)
            rating_log_objs = recipe_models.RatingLog.objects.filter(
                rated_recipe=wongnok_recipe_obj,
                rater=request.user
            )
            if len(rating_log_objs) == 1:
                is_already_rated = True
                rated_value = rating_log_objs[0].rating
            else:
                is_already_rated = False
                rated_value = None
            context = {}
            context['wongnok_recipe_obj'] = [
                wongnok_recipe_obj.auto_id,
                wongnok_recipe_obj.title,
                wongnok_recipe_obj.image_address,
                wongnok_recipe_obj.ingredient,
                wongnok_recipe_obj.step,
                wongnok_recipe_obj.duration,
                wongnok_recipe_obj.cooking_level,
                rating,
                wongnok_recipe_obj.owner.first_name + ' ' + wongnok_recipe_obj.owner.last_name,
                datetime.datetime.isoformat(wongnok_recipe_obj.updated_timestamp.astimezone(zoneinfo.ZoneInfo('Asia/Bangkok'))),
                request.user.email == wongnok_recipe_obj.owner.email,
                [item[0] for item in recipe_models.RatingLog._meta.get_field('rating').choices],
                is_already_rated,
                rated_value,
            ]
        else:
            recipe_id = request.GET.get('recipeID', None)
            rating = request.GET.get('rating', None)
            wongnok_recipe_obj = recipe_models.WongnokRecipe.objects.get(auto_id=recipe_id)
            context = {}
            context['wongnok_recipe_obj'] = [
                wongnok_recipe_obj.auto_id,
                wongnok_recipe_obj.title,
                wongnok_recipe_obj.image_address,
                wongnok_recipe_obj.ingredient,
                wongnok_recipe_obj.step,
                wongnok_recipe_obj.duration,
                wongnok_recipe_obj.cooking_level,
                rating,
                wongnok_recipe_obj.owner.first_name + ' ' + wongnok_recipe_obj.owner.last_name,
                datetime.datetime.isoformat(wongnok_recipe_obj.updated_timestamp.astimezone(zoneinfo.ZoneInfo('Asia/Bangkok'))),
            ]
        return render(request, 'recipe/view_recipe.html', context)
    elif request.method == 'POST':
        recipe_id = request.POST.get('inputRecipeID', None)
        input_rating = request.POST.get('inputRating', None)
        input_rating_non = request.POST.get('inputRatingNon', None)
        try:
            wongnok_recipe_obj = recipe_models.WongnokRecipe.objects.get(auto_id=recipe_id)
            if input_rating_non != None:
                return redirect(reverse('edit_my_recipe') + '?recipeID=' + recipe_id)
            else:                
                if (input_rating != None) and (input_rating != ''):
                    rating_log_obj = recipe_models.RatingLog(
                        rating=input_rating,
                        rated_recipe=wongnok_recipe_obj,
                        rater=request.user,
                        created_timestamp=datetime.datetime.now(datetime.timezone.utc)
                    )
                    rating_log_obj.save()
                    messages.error(request, 'Rating is success!')
                    return redirect('all_recipe')
                else:
                    messages.error(request, 'Rating is not be done!')
        except Exception as er:
            messages.error(request, str(er))
        return redirect('all_recipe')  
    

def my_recipe(request):
    context = {}
    wongnok_recipe_objs = recipe_models.WongnokRecipe.objects.filter(owner=request.user)
    context['wongnok_recipe_objs'] = []
    for obj in wongnok_recipe_objs:        
        _rating_log_objs = recipe_models.RatingLog.objects.filter(rated_recipe=obj.auto_id)
        ratings = [float(item.rating) for item in _rating_log_objs]
        rating = '%.2f' % float(sum(ratings) / len(ratings)) if len(ratings) != 0 else '0.00'
        context['wongnok_recipe_objs'].append(
            [
                obj.auto_id,
                obj.title,
                obj.duration,
                obj.cooking_level,
                rating
            ]
        )
    return render(request, 'recipe/my_recipe.html', context)

def create_my_recipe(request):
    if request.method == 'GET':
        context = {}
        context['duration_choices'] = [item[0] for item in recipe_models.WongnokRecipe._meta.get_field('duration').choices]
        context['cooking_level_choices'] = [item[0] for item in recipe_models.WongnokRecipe._meta.get_field('cooking_level').choices]
        return render(request, 'recipe/create_my_recipe.html', context)
    elif request.method == 'POST':
        title = request.POST.get('inputTitle', None)
        image_address = request.POST.get('inputImageAddress', None)
        ingredient = request.POST.get('inputIngredient', None)
        step = request.POST.get('inputStep', None)
        duration = request.POST.get('inputDuration', None)
        cooking_level = request.POST.get('inputCookingLevel', None)
        try:
            if (title != None) and (image_address != None) and (ingredient != None) and (step != None) and (duration != None) and (cooking_level != None):
                wongnok_recipe_obj = recipe_models.WongnokRecipe(
                    title=title,
                    image_address=image_address,
                    ingredient=ingredient,
                    step=step,
                    duration=duration,
                    cooking_level=cooking_level,
                    owner=request.user,
                    updated_timestamp=datetime.datetime.now(datetime.timezone.utc)
                )  
                wongnok_recipe_obj.save()
                messages.error(request, 'creating is success!')
                return redirect('my_recipe')
            else:
                messages.error(request, 'something is missing')
        except Exception as er:
            messages.error(request, str(er))
        return redirect('create_my_recipe')  

def edit_my_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipeID', None)
        wongnok_recipe_obj = recipe_models.WongnokRecipe.objects.get(auto_id=recipe_id)
        context = {}
        context['wongnok_recipe_obj'] = [
            wongnok_recipe_obj.auto_id,
            wongnok_recipe_obj.title,
            wongnok_recipe_obj.image_address,
            wongnok_recipe_obj.ingredient,
            wongnok_recipe_obj.step,
            wongnok_recipe_obj.duration,
            wongnok_recipe_obj.cooking_level
        ]
        context['duration_choices'] = [item[0] for item in recipe_models.WongnokRecipe._meta.get_field('duration').choices]
        context['cooking_level_choices'] = [item[0] for item in recipe_models.WongnokRecipe._meta.get_field('cooking_level').choices]
        return render(request, 'recipe/edit_my_recipe.html', context)
    elif request.method == 'POST':
        recipe_id = request.POST.get('inputRecipeID', None)
        title = request.POST.get('inputTitle', None)
        image_address = request.POST.get('inputImageAddress', None)
        ingredient = request.POST.get('inputIngredient', None)
        step = request.POST.get('inputStep', None)
        duration = request.POST.get('inputDuration', None)
        cooking_level = request.POST.get('inputCookingLevel', None)
        try:
            wongnok_recipe_obj = recipe_models.WongnokRecipe.objects.get(auto_id=recipe_id)
            if (title != None) and (image_address != None) and (ingredient != None) and (step != None) and (duration != None) and (cooking_level != None):
                wongnok_recipe_obj.title=title
                wongnok_recipe_obj.image_address=image_address
                wongnok_recipe_obj.ingredient=ingredient
                wongnok_recipe_obj.step=step
                wongnok_recipe_obj.duration=duration
                wongnok_recipe_obj.cooking_level=cooking_level
                wongnok_recipe_obj.save()
                messages.error(request, 'updating is success!')
                return redirect('my_recipe')
            else:
                messages.error(request, 'something is missing')
        except Exception as er:
            messages.error(request, str(er))
        return redirect('my_recipe')  

def delete_my_recipe(request):
    recipe_id = request.GET.get('recipeID', None)
    try:
        wongnok_recipe_obj = recipe_models.WongnokRecipe.objects.get(auto_id=recipe_id)
        wongnok_recipe_obj.delete()
        messages.error(request, 'deleting is success!')
    except Exception as er:
            messages.error(request, str(er))
    return redirect('my_recipe')  
    
        
        