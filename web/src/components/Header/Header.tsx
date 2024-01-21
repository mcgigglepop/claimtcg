import logoSevenLight from '../../assets/logo-7-light.png'
import logoSeven from '../../assets/logo-7.png'

const Header: React.FC = () => {
    return (
        <header className="transparent header-light scroll-light">
      <div className="container">
        <div className="row">
          <div className="col-md-12">
            <div className="de-flex sm-pt10">
              <div className="de-flex-col">
                <div className="de-flex-col">
                  <div id="logo">
                    <a href="!#">
                      <img alt="" className="logo" src={logoSevenLight} />
                      <img alt="" className="logo-2" src={logoSeven} />
                    </a>
                  </div>
                </div>
              </div>
              <div className="de-flex-col header-col-mid">
                <ul id="mainmenu">
                  <li>
                    <a href="!#">
                      Explore<span></span>
                    </a>
                  </li>
                  <li>
                    <a href="!#">
                      About Us<span></span>
                    </a>
                  </li>
                  <li>
                    <a href="!#">
                      FAQ<span></span>
                    </a>
                  </li>
                  <li>
                    <a href="!#">
                      Login<span></span>
                    </a>
                  </li>
                  <li>
                    <a href="!#">
                      Register<span></span>
                    </a>
                  </li>
                  <li className="d-block d-md-none">
                    <a href="!#">
                      Sell With Us<span></span>
                    </a>
                  </li>
                </ul>
                <div className="menu_side_area">
                  <a
                    href="!#"
                    className="btn-main btn-wallet"
                  >
                    <i className="icon_wallet_alt"></i>
                    <span>Sell With Us</span>
                  </a>
                  <span id="menu-btn"></span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    );
}

export default Header;