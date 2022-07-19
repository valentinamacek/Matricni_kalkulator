%rebase('base.tpl')
 det (<table class="matrika">                                 )    
      % for vrstica in  matrika.spremeni_obliko_matrike(): 
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table>
=
 {{ determinanta }}