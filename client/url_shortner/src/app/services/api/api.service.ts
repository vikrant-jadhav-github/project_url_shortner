import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  public url: string = 'http://localhost:8000/api/v1/';

  constructor() { }
  
}
