%rebase('base.tpl')
<div class="p-4">
Navodila:
<ul>
<li>elementi matrike naj bodo realna števila ( lahko napišeš cela števila, števila z decimalno piko, ulomke)</li>
<li>za vsakim željenim elementom zapiši presledek </li>
<li>Znak za novo vrstico je: <strong> ; </strong> </li> 
</ul>
<form method="POST">
 <input name="matrika" placeholder="matrika">
% if "matrika" in napake:
   {{ napake["matrika"] }}
% end
<button type="submit" class="btn btn-secondary"> Dodaj </button>
</form>
<a href="/" >Prekliči</a>
</div>