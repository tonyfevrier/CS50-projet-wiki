- `créer une url, une vue pour un titre d'entrée`
- `créer l'html associé et organiser la page avec titre et contenu`
- `le search doit mener vers entry`
- `créer la page d'erreur si le TITRE pas correct`
- `création de la page query error, url`
- `créer la vue qui checke si la chaine est une sous chaine d'entrées existantes : éventuellement passer la query dans l'url si besoin.`
- `créer une page avec input (newpage)`
- `faire la vue de newpage`
- `Bug: pourquoi ne voit pas newpage.html.`
- `ajouter le message d'erreur à newpage`
- `Bug : j'ai créé une page avec Test, sur index page, le lien cliqué m'envoie sur la page d'erreur. Idem pour le search.`
- `view de editpage : passer le contenu existant`
- `créer une vue et url pour recevoir le nouveau contenu de edit et l'enregistrer.`
- `Bug : comprendre pourquoi le contenu n'est pas enregistré.`
- `Ecrire deux tests unitaires testant la création et l'édition d'une page : peut aider à débugger le test.`
- `random page : créer une url random et une vue qui prend les entries et en choisit une au pif, puis redirige vers la page`
- `écriture d'un module markdown : tester le fonctionnement`
- `modifier ul li avec ^$ et multiline à la place des \n{2} : il semble buggé car je termine pas par \n. Voir peut-être en 2 temps : d'abord mettre les li puis repérer le li de début et le /li de fin pour l'entourer de ul. Pb compris : quand je remplace les p ça enlève les double \n\n avec mon code du coup on ne voit plus s'il y a un ou plusieurs sauts de lignes.`
- `bug quand je clique sur send, le texte dans la fenêtre à éditer rajoute des sauts de ligne : ca semble être au moment où defautstorage save le contenu`
- `si bug pas trouvé, dans les tests enlever les \n `
- `tester faire un defaultst.save de "test\n\n pour voir si ça les convertit en \r\n"`
- `en cas d'espace inséré par erreur dans l'input titre, il faudrait nettoyer ces espaces (voir si re le permet)` 