from . import bp as app
from app.blueprints.main.models import User, AllPokemon, UserPokemon, Move, PokemonMove
from app import db, login_manager
from flask import redirect, url_for, render_template, request, flash
from flask_login import current_user, login_required
from random import randint


@app.route('/')
def home():
    random_ids = [randint(1, 900) for x in range(4)]
    display_pokemon = {}
    for id in random_ids:
        random_pokemon = AllPokemon.query.filter_by(id=id).first()
        display_pokemon[id] = random_pokemon
    return render_template('home.html.j2', user=current_user, pokemon=display_pokemon)


@app.route('/pokemon/<id>')
@login_required
def pokemon_by_id(id):
    pokemon = AllPokemon.query.get(int(id))
    return render_template('pokemon_single.html.j2', pokemon=pokemon)

@app.route('/pokemon/choose', methods= ["GET", "POST"])
@login_required
def choose_pokemon():

    pokemon_id= int(request.form['pokemon'])

    pokemon = AllPokemon.query.get(pokemon_id)
    user_id = current_user.id 
    pokemon_id = pokemon.id
    name = pokemon.name
    type1 = pokemon.type1
    type2 = pokemon.type2
    if pokemon.ability2:
        ability_num = randint(1,2)
    elif pokemon.ability3:
        ability_num = randint(1,3)
    else:
        ability_num = 1
    ability_str = 'ability' + str(ability_num)
    ability = getattr(pokemon, ability_str)
    """
    
    move_list = [r._asdict() for r in (PokemonMove.query.filter_by(pokemon_id=pokemon_id))]
    move1 = move_list[1]
    if len(move_list) == 2:
        move2 = move_list[randint(1, 749)]
        while move2 == move1 or move2 not in move_list:
            move2 = move_list[randint(1, len(move_list)-1)]
    elif len(move_list) == 3:
        move2 = move_list[randint(1, len(move_list)-1)]
        move3 = move_list[randint(1, len(move_list)-1)]
        while move2 == move1:
            move2 = move_list[randint(1, len(move_list)-1)]
        while move3 == move1 or move3 == move2:
            move3 = move_list[randint(1, len(move_list)-1)]
    elif len(move_list) >= 4:
        move2 = move_list[randint(1, len(move_list)-1)]
        move3 = move_list[randint(1, len(move_list)-1)]
        move4 = move_list[randint(1, len(move_list)-1)]
        while move2 == move1:
            move2 = move_list[randint(1, len(move_list)-1)]
        while move3 == move1 or move3 == move2:
            move3 = move_list[randint(1, len(move_list)-1)]
        while move4 == move1 or move4 == move2 or move4 == move3:
            move4 = move_list[randint(1, len(move_list)-1)]

    """
    move1=1
    shiny_chance = randint(1,100)
    if shiny_chance == 100:
        sprite = pokemon.shiny_sprite
    else:
        sprite = pokemon.reg_sprite
    new_pokemon = UserPokemon(user_id=user_id, pokemon_id=pokemon_id, name=name,
    type1=type1, type2=type2, ability=ability, sprite=sprite, move1=move1)
    db.session.add(new_pokemon)
    db.session.commit()
    flash(f'{new_pokemon.name.title()} added to your PC', 'success')
    return redirect(url_for('main.your_pc'))

@app.route('/your_pc')
@login_required
def your_pc():
    return render_template('your_pc.html.j2', user=current_user)

@app.route('/your_pc/<id>')
@login_required
def user_pokemon_by_id(id):
    pokemon = UserPokemon.query.get(int(id))
    print(id)
    return render_template('user_single_pokemon.html.j2', pokemon=pokemon, user=current_user)
