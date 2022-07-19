%rebase('base.tpl')
 <table class="matrika">                                     T
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
      % for vrstica in  transponirana.spremeni_obliko_matrike():
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table>