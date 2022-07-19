%rebase('base.tpl')
 <table class="matrika">                                     
      % for vrstica in  matrika.spremeni_obliko_matrike(): 
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table>
Prirejenka:
 <table class="matrika"> 
      % for vrstica in  prirejena.spremeni_obliko_matrike():
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table>