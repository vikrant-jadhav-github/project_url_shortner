import { ApiService } from './../api/api.service';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UrlService {

  private shortenedUrlSubject = new BehaviorSubject<string>('');
  public shortenedUrl = this.shortenedUrlSubject.asObservable();

  public endPoint = this.apiService.url + 'url/';

  constructor(private httpClient: HttpClient, private apiService: ApiService, private toastr: ToastrService) { }

  public getShortenedUrl(url: string) {

    this.httpClient.post(this.endPoint, { url: url }).subscribe(
      (response: any) => {
        if(response.status === 201)
        {
          this.shortenedUrlSubject.next(response.url);
          this.toastr.success('URL shortened successfully', 'Success');
          return;
        }
        this.toastr.error('Something went wrong, Please try again after some time', 'Error');
      }
    )
  }

}
