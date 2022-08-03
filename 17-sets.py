# set = collection which is unordered, unindexed. No duplicate values
# => 중복 허용 X (중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용하기도 한다.)
# => 순서가 없다 (인덱싱으로 값을 얻을 수 없다.)

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils) # update : 값 여러 개 추가하기
# dinner_table = utensils.union(dishes) # union : 합집합
# dinner_table = utensils.intersection(dishes) # intersection : 교집합
# dinner_table = utensils.difference(dishes) # difference : 차집합

for x in utensils:
  print(x)