import React from 'react';
import {SafeAreaView, Pressable, Text} from 'react-native';
import {useDispatch, useSelector} from 'react-redux';
import Header from '../../components/Header/Header';
import globalStyle from '../../assets/styles/globalStyle';
import {updateFirstName} from '../../redux/reducers/User';

const Home = () => {
  const user = useSelector(state => state.user);
  const dispatch = useDispatch();

  return (
    <SafeAreaView style={[globalStyle.backgroundWhite, globalStyle.flex]}>
      <Header title={user.firstName + ' ' + user.lastName} />
      <Pressable onPress={() => dispatch(updateFirstName({firstName: 'N'}))}>
        <Text>Press me</Text>
      </Pressable>
    </SafeAreaView>
  );
};

export default Home;
