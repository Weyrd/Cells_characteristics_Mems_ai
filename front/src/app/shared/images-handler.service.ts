import {Injectable} from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ImagesHandlerService {
  static imagesUploaded: any[] = [];

  constructor() {
  }

  static addImage(image: any): void {
    ImagesHandlerService.imagesUploaded.push(image);
  }


}
