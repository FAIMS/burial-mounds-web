
// $('#bigImage').replaceWith()


function makeBigImage(element, elementSRC, caption, captionHREF){
	if (element == 'iframe'){
		$("#bigImage").html("<iframe id='IframeCanvas' height='100%' width='100%' style='border-width: 0px;' src='"+elementSRC+"'></iframe>");
		//$("#imgCanvas").css('padding-right', 0);
		$("#imgCanvas").css('height', 420);
		$("#bigImage").css('height', 375);		

	} else {
		$("#bigImage").html("<img style='height:375px' src='"+elementSRC+"'/>");
		$("#imgCanvas").css('height', 420);
		$("#bigImage").css('height', 375);	
	}



	if (captionHREF == ''){
		$("#imgCaption").html("<span>"+caption+"</span>");
	} else {
		$("#imgCaption").html("<a target='_blank' href='"+captionHREF+"'>"+caption+"</a>");
	}
	

	//alert(element + elementSRC + caption + captionHREF);
}