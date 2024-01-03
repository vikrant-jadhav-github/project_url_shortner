import { UrlService } from './services/url/url.service';
import { Component } from '@angular/core';
import { Clipboard } from '@angular/cdk/clipboard';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {

  public enteredUrl: string = '';
  public shortenedUrl: string = '';

  constructor(private urlService: UrlService, private clipboard: Clipboard, private toastr: ToastrService) {}

  public shortUrl(url: string) {

    if(!url){
      this.toastr.info('Please enter a URL', 'Guide');
      return;
    }

    const urlPattern = /^(http|https):\/\//;
    
    if(!urlPattern.test(this.enteredUrl)){
      this.enteredUrl = '';
      this.toastr.info('Please enter a valid URL', 'Guide');
      return;
    }
    
    this.urlService.getShortenedUrl(url);

    this.urlService.shortenedUrl.subscribe(
      (response: string) => {
        this.shortenedUrl = response;
      }
    )

    this.enteredUrl = '';

  }

  public copyUrl(){
    this.clipboard.copy(this.shortenedUrl);
    this.toastr.success('Copied to clipboard', 'Success');
  }

}
