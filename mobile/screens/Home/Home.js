import React from 'react';
import {SafeAreaView, Text, View} from 'react-native';

import globalStyle from '../../assets/styles/globalStyle';

const Home = () => {
  return (
    <SafeAreaView style={[globalStyle.backgroundWhite, globalStyle.flex]}>
      <View>
        <Text>Hello World!</Text>
      </View>
    </SafeAreaView>
  );
};

export default Home;
