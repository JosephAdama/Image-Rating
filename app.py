import os
import cv2

def rate_and_move_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)
            
            # Resize the image to fit within the screen size
            screen_height, screen_width, _ = image.shape
            max_display_height = 360  # Adjust as needed
            max_display_width = 640  # Adjust as needed
            
            if screen_height > max_display_height or screen_width > max_display_width:
                resize_ratio = min(max_display_width / screen_width, max_display_height / screen_height)
                new_width = int(screen_width * resize_ratio)
                new_height = int(screen_height * resize_ratio)
                image = cv2.resize(image, (new_width, new_height))
            
            cv2.imshow("Image", image)
            print(f"Rate the image: {filename}")
            rating = cv2.waitKey(0) - 48  # Convert key press to integer
            
            if 1 <= rating <= 5:
                rating_folder = os.path.join(output_folder, str(rating))
                if not os.path.exists(rating_folder):
                    os.makedirs(rating_folder)
                new_image_path = os.path.join(rating_folder, filename)
                cv2.imwrite(new_image_path, image)
                print(f"Image '{filename}' saved with rating {rating}.\n")
            else:
                print("Invalid rating. Please enter a value between 1 and 5.\n")
            
            cv2.destroyAllWindows()

if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "sorted_images"
    rate_and_move_images(input_folder, output_folder)
