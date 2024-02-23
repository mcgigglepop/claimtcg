export const getFontFamily = (basefont = 'Inter', weight) => {
  switch (weight) {
    case '100':
      return `${basefont}-Thin`;
    case '200':
      return `${basefont}-ExtraLight`;
    case '300':
      return `${basefont}-Light`;
    case 'normal':
    case '400':
      return `${basefont}-Regular`;
    case '500':
      return `${basefont}-Medium`;
    case '600':
      return `${basefont}-SemiBold`;
    case 'bold':
    case '700':
      return `${basefont}-Bold`;
    case '800':
      return `${basefont}-ExtraBold`;
    case '900':
      return `${basefont}-Black`;
    default:
      return `${baseFont}-Regular`
  }
};
