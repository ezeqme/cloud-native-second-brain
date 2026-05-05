---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["GitOps Delivery"]
speakers: ["Chris Plank", "NatWest"]
sched_url: https://kccnceu2026.sched.com/event/2EG0J/cloud-native-theater-cloud-native-university-introduction-to-gitops-chris-plank-natwest
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+Introduction+to+GitOps+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Cloud Native University: Introduction to GitOps - Chris Plank, NatWest

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[GitOps Delivery]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Chris Plank, NatWest
- Schedule: https://kccnceu2026.sched.com/event/2EG0J/cloud-native-theater-cloud-native-university-introduction-to-gitops-chris-plank-natwest
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+Introduction+to+GitOps+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Cloud Native University: Introduction to GitOps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0J/cloud-native-theater-cloud-native-university-introduction-to-gitops-chris-plank-natwest
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+Introduction+to+GitOps+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=v3SkICW7_aw
- YouTube title: Cloud Native Theater | Cloud Native University: Introduction to GitOps - Chris Plank, NatWest
- Match score: 0.95
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-cloud-native-university-introduction-to-gitops/v3SkICW7_aw.txt
- Transcript chars: 8017
- Keywords: started, flux, better, gitops, developers, cluster, argo, simple, physical, connectivity, devops, control, environments, development, testing, starting, running, container

### Resumo baseado na transcript

I'm a CNCF platform engineering technical community group leader and I work for uh, one of the top four banks in the UK. So, this talk's going to be full of dinosaur prints and it's going to be full of dragons and tales of old. So, kind of focusing on that era of the 2000s onwards really, when the cloud came along, devops came along, Kubernetes came along. And CRDs, they're just a way of extending the Kubernetes API to define your own kind of resource types. If you want to know about GitOps properly, there's the free CNCF uh, learn sorry, Linux Foundation uh, training course on this.

### Excerpt da transcript

Uh, I'm Chris Plank. I'm a CNCF platform engineering technical community group leader and I work for uh, one of the top four banks in the UK. And I think you can guess where I come from, right? Which country? Um, I'm notorious for going over time. So, we'll have a bit of a laugh today. It's only 25 slides, Daniel. Should be fine. Uh, but let's see how this goes. We're going to go really, really fast. Really simple topic. Uh, I've been IT for 30 years. Think of me as a bit of a dinosaur. So, this talk's going to be full of dinosaur prints and it's going to be full of dragons and tales of old. But I'm not going to talk about mainframe punch cards. If you want to find out about that, there's a QR code there. You can go and follow it. But this is really a story of how we got to get ups and what get ups is. And it did start back in those mainframe days. You know, people used to take data and input into servers and mainframes and things like that. So, we're going to go from floppy disks all the way through to get ups.

And really the story's all about humans physically moving data to servers, right? And how we how we used to do that and what we do now in the kind of cloud era. And we went from floppy disks, we went to CDs. And CDs obviously took a lot more data, but it was still physical. People were still doing physical stuff and going into the data centers. Then we moved to even smaller but more capacity devices, the USB sticks. Again, more data but still physical. Then the internet came along. You know, I started my career in 1995. And when I started it, it was like the dial-up era, you know? Tales of old, you have to plug in your phone line into a modem and hear these weird sounds. And the networking was terrible. Then we had 64K. Could you imagine how long it would take to upload some of our docker images today over a 64K line, right? Be forever. Uh, so tales of dragons to the left. I'm not going to talk about everything before 1995. But if we go through that timeline, the things that started to evolve, we got ADSL, we got better connectivity.

The CSPs came out. We started getting direct connect connectivity into AWS, for example, and then to Google. And we got faster fiber optic. And I work for my RV, my motorhome. Um, I think I can't remember what they call it here. Uh, camping car. Uh, and I use Starlink. You know, and we've got fantastic speeds coming through Starlink now as well. 120 meg downloads and 80 meg uploads. Uh, way, way better than those old
