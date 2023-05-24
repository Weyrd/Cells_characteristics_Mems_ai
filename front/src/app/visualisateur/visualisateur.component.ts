import {Component, Input, Output} from '@angular/core';

@Component({
  selector: 'app-visualisateur',
  templateUrl: './visualisateur.component.html',
  styleUrls: ['./visualisateur.component.css']
})
export class VisualisateurComponent {
  @Input() private imagesUploaded: object[] = [];

  @Input()
  addImage(image: any): void {
    this.imagesUploaded.push(image);
  }

  getIfImagesUploaded(): number {
    let isImage = 0
    if (this.imagesUploaded.length >= 1) {
      isImage = 1;
    } else {

      isImage = 0;
    }
    return isImage;
  }

  getImagesUploaded(): any[] {
    return this.imagesUploaded;
  }

  @Output()
  resetImages() {
    this.imagesUploaded = [];
  }


}
