import React from 'react';
import {Image, View} from 'react-native';
import PropTypes from 'prop-types';

import Badge from '../Badge/Badge';
import Header from '../Header/Header';

import style from './style';

const SingleAuctionItem = props => {
  return (
    <View>
      <View>
        <Badge title={props.badgeTitle} />
        <Image source={{uri: props.uri}} style={style.image} />
      </View>
      <Header title={props.auctionTitle} type={3} color={'#0A043C'} />
      <Header title={'$' + props.price.toFixed(2)} type={3} color={'#156CF7'} />
    </View>
  );
};

SingleAuctionItem.propTypes = {
  uri: PropTypes.string.isRequired,
  badgeTitle: PropTypes.string.isRequired,
  auctionTitle: PropTypes.string.isRequired,
  price: PropTypes.number.isRequired,
};

export default SingleAuctionItem;
