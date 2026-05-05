---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Reliability + Operational Continuity"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: ["Vincent Batts", "Microsoft Azure"]
sched_url: https://kccncna2022.sched.com/event/182GH/unsung-hero-of-the-cloud-native-revolution-container-linux-then-and-now-vincent-batts-microsoft-azure
youtube_search_url: https://www.youtube.com/results?search_query=Unsung+Hero+Of+the+Cloud+Native+Revolution%3A+Container+Linux+Then+And+Now+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Unsung Hero Of the Cloud Native Revolution: Container Linux Then And Now - Vincent Batts, Microsoft Azure

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Vincent Batts, Microsoft Azure
- Schedule: https://kccncna2022.sched.com/event/182GH/unsung-hero-of-the-cloud-native-revolution-container-linux-then-and-now-vincent-batts-microsoft-azure
- Busca YouTube: https://www.youtube.com/results?search_query=Unsung+Hero+Of+the+Cloud+Native+Revolution%3A+Container+Linux+Then+And+Now+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Unsung Hero Of the Cloud Native Revolution: Container Linux Then And Now.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182GH/unsung-hero-of-the-cloud-native-revolution-container-linux-then-and-now-vincent-batts-microsoft-azure
- YouTube search: https://www.youtube.com/results?search_query=Unsung+Hero+Of+the+Cloud+Native+Revolution%3A+Container+Linux+Then+And+Now+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BhMExNw9904
- YouTube title: Unsung Hero Of the Cloud Native Revolution: Container Linux Then And Now - Vincent Batts
- Match score: 0.99
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/unsung-hero-of-the-cloud-native-revolution-container-linux-then-and-no/BhMExNw9904.txt
- Transcript chars: 27562
- Keywords: container, actually, around, upstream, whatever, whether, kernel, everybody, otherwise, deploy, packages, together, yourself, version, fedora, reboot, little, interesting

### Resumo baseado na transcript

um and y'all are spread out all over the room that's fine I honestly this is way more people than I was expecting at four o'clock on a Friday afternoon after a long week so thank you all for being here um in this talk the unsung hero of cloud native I'm going to talk to a little bit of history in a little bit of where we are in container linux's or linux's in general Linux High first I know a few of you I'm already seeing faces in um dot Cloud did the demo with the Python scripts of Docker in the summer and then by the Fall Winter we had the the emergence of the Go version of docker um and that there was kind of like some cross-pollinations in both directions

### Excerpt da transcript

um and y'all are spread out all over the room that's fine I honestly this is way more people than I was expecting at four o'clock on a Friday afternoon after a long week so thank you all for being here um in this talk the unsung hero of cloud native I'm going to talk to a little bit of history in a little bit of where we are in container linux's or linux's in general Linux High first I know a few of you I'm already seeing faces in here if you want to know me please reach out I love meeting new people all the time um I've been around in a couple of these different communities for quite a while um I lose track of how all these things overlap but for it this community particularly in the last 10 years have been involved in uh Docker since 2013 and then at some point FC and now if you've heard about the open container initiative specifications like how Registries even taught together how runtimes work how images are packed love playing with tar layers please reach out to commiserate most recently was with Ken folk and now for the last year and a half Ken Volk team is on with Microsoft azure um among the favorites their flat car container Linux so I'll go ahead and disclaim that biases or otherwise frustrations this is I like to keep things very objective but my most current and you know steel current affiliation is with flat car container Linux but I have been involved in aspects of a lot of things over the years so leave it at that um so first off container Linux all these nice little buzz words here with a little Bumble piece everywhere um what would you say would be a container Linux like actually what would y'all say container Linux means to you thin minimal whatever anybody else come on what purpose built use case specific builds hardened hardened you kind of want that from all of them maybe not exclusive to container linux's but again in the purpose built you know theme you start figuring out what that means and you harden it down um I put Ikea versus artisanal just because cattles versus pet kind of whatever but you go to you go to Ikea and it's a warehouse of mass built things and good luck but it's like mass produced and then anything RTS know when you see that this one thing doesn't quite look like the other you've now got something tailored not necessarily different than purpose built but we'll kind of get into that a little bit and the atomic Updates this is this gets into a kind of a a a theme here but first off like you have to kind of back up an
