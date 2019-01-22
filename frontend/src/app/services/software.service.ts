import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'


@Injectable({
  providedIn: 'root'
})
export class SoftwareService {

  private _listUrl = "http://127.0.0.1:8000/api/v1/software/"

constructor(public http: HttpClient) { }

getAll() {
  return this.http.get<any>(this._listUrl)
}

}
