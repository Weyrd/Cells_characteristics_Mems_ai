import {Component, Input, Output} from '@angular/core';

@Component({
  selector: 'app-visualisateur',
  templateUrl: './visualisateur.component.html',
  styleUrls: ['./visualisateur.component.css']
})
export class VisualisateurComponent {
  private imagesUploaded: object[] = [];
  @Input() title: string = "";

  @Input()
  addImage(image: any): void {
    this.imagesUploaded.push(image);
    console.log("[--] Image added")
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
    console.log("[--] Reset images")
    this.imagesUploaded = [];
  }


}
