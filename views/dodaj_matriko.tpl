%rebase('base.tpl')
Navodila:
Vnesi elemente nove matrike, tako da:
<ul>
<li> napišeš željen element za njim pa presledek </li>
<li> znak za novo vrstico je: ; 
</ul>
<form method="POST">
 <input name="matrika" placeholder="matrika">
% if "matrika" in napake:
   {{ napake["matrika"] }}
% end
<button type="submit"> Dodaj </button>
</form>