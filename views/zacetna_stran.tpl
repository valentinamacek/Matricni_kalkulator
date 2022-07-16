%rebase('base.tpl')
    <h1>Dobrodošli v matričnem kalkulatorju</h1>

    Vaše matrike:
    % for matrika in matrike:
        <table class="matrika">
       % for vrstica in  matrika.matrika:
            <tr>
          % for element in vrstica:
          <td>    {{ spremeni_obliko(element) }}  </td>
          % end
            </tr>
       % end
        </table>
    % end
    
  