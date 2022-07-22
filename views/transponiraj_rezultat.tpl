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
        <div class="col-sm-auto"> T </div>
        <div class="col-sm-auto"> 
        <table>
        <tr> <td> </td>
         </tr>
        <tr> <td> </td>
         </tr>
        <tr> <td> </td>
         </tr>
        <tr>
        <td>=</td>
        </tr>
        </table>
        </div>
        <div class="col-md-auto">
        <table class="matrika"> 
            % for vrstica in  transponirana.spremeni_obliko_matrike():
                <tr>
                % for element in vrstica:
                <td>    {{ element }}  </td>
                % end
                </tr>
            % end
        </table>
        </div>
    </div>
