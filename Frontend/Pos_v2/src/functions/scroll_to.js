export default function scrollTo(selectorClass)  {
  document.querySelector(`${selectorClass}`).scrollIntoView({block: "start", behavior: "smooth"})
}
