import { StyleSheet, Dimensions } from 'react-native'
import {
  blanco,
  blancoTotal,
  darkGrey,
  midGrey,
  acento,
  primario,
  bodyGrey,
  bodyFontSize,
  fontSizeLarger,
  fontSizeLarge,
  fontSizeMedium,
  fontSizeSmall,
  fontSizeSmaller,
  fontSizeTiny,
  conFontSize,
  gridHeight,
  fontWeightBold,
  fontWeightLight,
  globalPaddingTiny,
  globalPaddingSmall,
  globalPadding,
  globalPaddingMedium,
  globalPaddingLarge,
  globalPaddingLarger,
  globalPaddingJumbo,
} from './vars'

export const fullWidth = Dimensions.get('window').width
export const fullHeight = Dimensions.get('window').height

const GlobalStyles = {
  HomeContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    height: '100%',
    width: '100%',
    position: 'absolute',
  },
  AppBackground: {
    backgroundColor: blanco,
  },
  homeScrim: {
    backgroundColor: darkGrey,
    opacity: 0.2,
    height: '100%',
    zIndex: 1,
  },
  fullScreenView: {
    height: fullHeight,
    width: fullWidth,
  },
  logoImage: {
    width: 200,
    height: 200,
    resizeMode: 'contain',
  },
  logoContainer: {
    top: 0,
  },
  heroText: {
    color: blanco,
    fontWeight: "800",
    paddingVertical: globalPaddingMedium,
  },
  accentButton: {
    backgroundColor: primario,
    borderRadius: 20,
    paddingHorizontal: globalPaddingLarge,
    paddingVertical: globalPaddingSmall,
    zIndex:5,
  },
  buttonStyle: {
    fontSize: bodyFontSize,
    color: bodyGrey,
    fontWeight: "800",
  },
  alignBottom: {
    alignContent: 'flex-end',
  },
  heroImage: {
    width: '100%',
    height: '100%',
    resizeMode: 'cover',
    zIndex: 0,
    position: 'absolute',
  }
}

function createStyles(overrides = {}) {
  return StyleSheet.create({...GlobalStyles, ...overrides})
}
export default {
  createStyles,
}
