%rebase('base.tpl')
<div class="row justify-content-md-center gx-3">
    <div class="col-md-auto">
    <table class="matrika">                                     
        % for vrstica in  matrika.spremeni_obliko_matrike(): 
            <tr>
            % for element in vrstica:
            <td>    {{ element }}  </td>
            % end
            </tr>
        % end
        </table>
    </div>
    <div class="col-sm-auto"> -1 </div>
    <div class="col-sm-auto justify-content-sm-center"> = </div>
    <div class="col-sm-auto"> 
    <table class="matrika"> 
        % for vrstica in  inverz.spremeni_obliko_matrike():
            <tr>
            % for element in vrstica:
            <td>    {{ element }}  </td>
            % end
            </tr>
        % end
        </table>
    </div>
</div>