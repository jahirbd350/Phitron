let checkFriends = (array) => {
  let bigFriend = array[0];
  for (let i = 0; i < array.length; i++) {
    if (array[i].length > bigFriend.length) {
      bigFriend = array[i];
    }
  }
  return bigFriend;
};

let friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];
let bigFriend = checkFriends(friends);

console.log(bigFriend);
