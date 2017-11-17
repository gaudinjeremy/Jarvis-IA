#t!/bin/bash

#MODULE IA : Intelligence Aléatoire pour Jarvis

# $1 : la fonction
# $2 : le plugin
# $3 : la clef
# $4 : la valeur
jv_ia(){

    say "$(python $ia_path $1 $2 $3 $4)"
}
