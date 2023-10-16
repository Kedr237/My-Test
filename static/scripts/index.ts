function setElement(el: HTMLElement) {
  const text: string = el.textContent as string
  window.location.replace(text)
}