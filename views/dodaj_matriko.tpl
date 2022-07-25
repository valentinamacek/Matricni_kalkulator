%rebase('base.tpl')
Navodila:
Elementi matrike naj bodo realna števila.
Vnesi jih, tako da:
<ul>
<li> napišeš željen element za njim pa presledek </li>
</ul>
Znak za novo vrstico je: <strong> ; </strong>
<form method="POST">
 <input name="matrika" placeholder="matrika">
% if "matrika" in napake:
   {{ napake["matrika"] }}
% end
<button type="submit"> Dodaj </button>
</form>