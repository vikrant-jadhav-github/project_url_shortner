import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  public endPoint: string = 'http://localhost:8000/api/v1/url/';

  constructor() { }
  
}
