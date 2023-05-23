import {Component} from '@angular/core';
import {ImagesHandlerService} from '../shared/images-handler.service';

@Component({
  selector: 'app-drag-and-drop',
  templateUrl: './drag-and-drop.component.html',
  styleUrls: ['./drag-and-drop.component.css']
})
export class DragAndDropComponent {
  isFileOverContainer: boolean = false;
  isFileDragging: boolean = false;


  onDragOverContainer(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isFileOverContainer = true;
  }

  onDragOver(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isFileDragging = true;
  }

  onDragLeave(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isFileOverContainer = false;
    this.isFileDragging = false;

  }

  onDrop(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isFileOverContainer = false;
    this.isFileDragging = false;


    const files = event.dataTransfer?.files;
    const filesList: File[] = [];
    if (files) {
      for (let i = 0; i < files.length; i++) {
        filesList.push(files[i]);
      }
      this.readFile(filesList);

      console.log("Number image upload : ", ImagesHandlerService.imagesUploaded.length, "\nList :", ImagesHandlerService.imagesUploaded)

    }
  }


  private readFile(files: File[]): void {
    files.forEach((file: File) => {
      const reader = new FileReader();

      reader.onload = (e: ProgressEvent<FileReader>) => {
        const imageUrl = e.target?.result as string;

        const img = new Image();
        img.onload = () => {
          const imageSize = {
            width: img.width,
            height: img.height
          };
          let image = {"url": imageUrl, "size": imageSize}
          ImagesHandlerService.addImage(image);

        };
        img.src = imageUrl;

      };
      reader.readAsDataURL(file);

    });

  }

}
