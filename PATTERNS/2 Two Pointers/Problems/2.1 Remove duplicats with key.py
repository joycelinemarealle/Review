from distutils.dir_util import remove_tree


def remove_element(arr,key):
    nextElement = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement +=1
    return nextElement

if __name__ == "__main__":
    print(remove_element([2,11,2,2,1],3))