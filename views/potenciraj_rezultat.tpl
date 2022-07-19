%rebase('base.tpl')
%if isinstance(rezultat, Matrika):
<table class="matrika">                                    {{ stopnja }}
      % for vrstica in  matrika.spremeni_obliko_matrike():
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table>
=
<table class="matrika">                                    
      % for vrstica in  rezultat.spremeni_obliko_matrike():
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table> 
%else:
 Vnesi nenegativno celo stevilo
%end 