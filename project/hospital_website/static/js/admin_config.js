

function copy_img_tag(){
    navigator.clipboard.writeText(`<img src='${self.dataset.id_data}' />`);
}