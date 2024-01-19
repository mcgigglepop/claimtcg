import logoLight from '../../assets/logo-light.png';
import logo from '../../assets/logo.png';
import './Header.css';

export default function Header() {
  return (
    <header className="transparent header-light scroll-light">
        <div className="container">
            <div className="row">
                <div className="col-md-12">
                    <div className="de-flex sm-pt10">
                        <div className="de-flex-col">
                            <div className="de-flex-col">
                                <div id="logo">
                                    <a href="index.html">
                                        <img alt="" className="logo" src={logoLight} />
                                        <img alt="" className="logo-2" src={logo} />
                                    </a>
                                </div>
                            </div>
                        </div>
                        <div className="de-flex-col header-col-mid">
                            <ul id="mainmenu">
                                <li>
                                    <a href="index.html">Home<span></span></a>
                                    
                                </li>
                            </ul>
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
  );
}