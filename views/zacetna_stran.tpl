% rebase('base.tpl')
    <h1>Dobrodošli v matričnem kalkulatorju</h1>

    Vaše matrike:
    %for matrika in matrike:
    <div align=center>
        <table class="matrika">
    %   for vrstica in  matrika.matrika:
            <tr>
    %       for element in vrstica:
                <td> {{ element }}</td>
            </tr>
        </table>
    </div>
    %end