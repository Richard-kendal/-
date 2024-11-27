import time

def burn_fuse(fuse):
    total_time = 3600  
    burn_rate = total_time / len(fuse)  
    for segment in fuse:
        time.sleep(burn_rate)  
        if time.time() - start_time >= 2700:  

            return time.time() - start_time

fuse1 = [1] * 3600  
fuse2 = [1] * 3600  

start_time = time.time()
burn_time1 = burn_fuse(fuse1)
burn_time2 = burn_fuse(fuse2)

print(f"Фитиль 1 сгорел за: {burn_time1 / 60:.2f} минут")
print(f"Фитиль 2 сгорел за: {burn_time2 / 60:.2f} минут")
print(f"Отмерили 45 минут")

