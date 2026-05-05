---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Emerging + Advanced"
themes: ["Emerging + Advanced"]
speakers: ["Miguel Angel Ajo", "Red Hat"]
sched_url: https://kccnceu2025.sched.com/event/1txFD/a-cloud-native-workflow-for-hardware-in-the-loop-software-development-miguel-angel-ajo-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=A+Cloud+Native+Workflow+for+Hardware-in-the-Loop+Software+Development+CNCF+KubeCon+2025
slides: []
status: parsed
---

# A Cloud Native Workflow for Hardware-in-the-Loop Software Development - Miguel Angel Ajo, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Emerging + Advanced]]
- País/cidade: United Kingdom / London
- Speakers: Miguel Angel Ajo, Red Hat
- Schedule: https://kccnceu2025.sched.com/event/1txFD/a-cloud-native-workflow-for-hardware-in-the-loop-software-development-miguel-angel-ajo-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=A+Cloud+Native+Workflow+for+Hardware-in-the-Loop+Software+Development+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre A Cloud Native Workflow for Hardware-in-the-Loop Software Development.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFD/a-cloud-native-workflow-for-hardware-in-the-loop-software-development-miguel-angel-ajo-red-hat
- YouTube search: https://www.youtube.com/results?search_query=A+Cloud+Native+Workflow+for+Hardware-in-the-Loop+Software+Development+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=40OmDwTgl1A
- YouTube title: A Cloud Native Workflow for Hardware-in-the-Loop Software Development - Miguel Angel Ajo, Red Hat
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/a-cloud-native-workflow-for-hardware-in-the-loop-software-development/40OmDwTgl1A.txt
- Transcript chars: 20028
- Keywords: hardware, device, testing, drivers, working, cluster, everything, developer, starter, driver, interfaces, connect, tecton, client, exporter, serial, devices, framework

### Resumo baseado na transcript

Um, I know it's, uh, a little bit a topic a little bit different from everything that we normally have at CubeCon, but yeah, I wanted to see how it could go. Um, so this talk is about uh hardware in the loop testing with Kubernetes. Um well, this part is written in Python, but the server side part is written in Go because it works much better with the Go with the uh Kubernetes ecosystem. In this case, we have a storage device that we can control for the device. I think I don't have time to go through through the details but it's it's very uh it's very easy to to write a a driver and okay let's get into the demo side of things. Let me first explain what what I have deployed in in Kubernetes uh together with jump starter.

### Excerpt da transcript

Hi. So, um, welcome to this presentation. Thank you for coming. Um, I know it's, uh, a little bit a topic a little bit different from everything that we normally have at CubeCon, but yeah, I wanted to see how it could go. Um, so this talk is about uh hardware in the loop testing with Kubernetes. Um, So first uh yeah I I want to to clarify what I mean with hardware in the loop. So hardware in the loop is the technique or sometimes art of um testing uh with hardware in your life cycle. um to make sure that your your software is being test uh with the final hardware or at least a subset of that hardware in your lab. Um and the idea is that you simulate part of the environment or to to make sure that you can reproduce um something that works. So in companies uh where I've been when there where there is no hardware in the loop testing uh this is how it looks. Um so no maybe you have different variants of your devices and when you are going to make a release of your framework uh you need to test it on all of them and make sure that everything is fine.

do lots of manual testing and that doesn't scale well. Um so and and without a good testing strategy, we all know what happens. Um you you know all the first ones. Uh so stuff that used to work doesn't work anymore. It's difficult to figure out uh what's um what's really happening. you cannot meet your your deadlines. But in the case of of hardware and the physical world, sometimes it's even worse. Something called explode or crash or well yeah um so in the software industry this is I mean we have this very well figured out. we have a a good landscape of options uh that we can use to make sure that um everything is under control at every point of the development process. But I mean what what happens with hardware? Uh it hardware is not as easy to manage as VMs, containers. Um normally you don't have out of band management management. Sometimes you have but it's it's very rare. And you have tons of different interfaces uh like canvases, video inputs, video outputs, uh human interfaces. Um there are many many many options.

I would like to ask uh to the audience if um uh if in your company do you build any anything with embedded devices? Um okay nice. And do you already have any kind of uh hardware in the loop testing? Okay. And are you happy with what you have? Okay. Okay, nice. So, uh so let me tell you about uh our our project and what we have been working on. The the name of the project is is Yams Arthur and uh
