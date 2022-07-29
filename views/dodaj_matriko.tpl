%rebase('base.tpl')
Navodila:
<ul>
<li>elementi matrike naj bodo realna števila</li>
<li>za vsakim željenim elementom zapiši presledek </li>
<li>Znak za novo vrstico je: <strong> ; </strong> </li> 
</ul>
<form method="POST">
 <input name="matrika" placeholder="matrika">
% if "matrika" in napake:
   {{ napake["matrika"] }}
% end
<button type="submit"> Dodaj </button>
</form>
<a href="/" >Prekliči</a>