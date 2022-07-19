%rebase('base.tpl')
 <table class="matrika">                                     
      % for vrstica in  matrika1.spremeni_obliko_matrike(): 
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table>
*
 <table class="matrika"> 
      % for vrstica in  matrika2.spremeni_obliko_matrike():
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table>
=
 <table class="matrika"> 
      % for vrstica in  produkt.spremeni_obliko_matrike():
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table>