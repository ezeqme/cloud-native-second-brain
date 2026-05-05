---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["Felicitas Pojtinger", "Loophole Labs"]
sched_url: https://kccncna2024.sched.com/event/1i7l2/building-reliable-cross-cloud-kubernetes-clusters-on-spot-instances-with-drafter-and-pvm-felicitas-pojtinger-loophole-labs
youtube_search_url: https://www.youtube.com/results?search_query=Building+Reliable+Cross-Cloud+Kubernetes+Clusters+on+Spot+Instances+with+Drafter+and+PVM+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Building Reliable Cross-Cloud Kubernetes Clusters on Spot Instances with Drafter and PVM - Felicitas Pojtinger, Loophole Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Felicitas Pojtinger, Loophole Labs
- Schedule: https://kccncna2024.sched.com/event/1i7l2/building-reliable-cross-cloud-kubernetes-clusters-on-spot-instances-with-drafter-and-pvm-felicitas-pojtinger-loophole-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Reliable+Cross-Cloud+Kubernetes+Clusters+on+Spot+Instances+with+Drafter+and+PVM+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Building Reliable Cross-Cloud Kubernetes Clusters on Spot Instances with Drafter and PVM.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7l2/building-reliable-cross-cloud-kubernetes-clusters-on-spot-instances-with-drafter-and-pvm-felicitas-pojtinger-loophole-labs
- YouTube search: https://www.youtube.com/results?search_query=Building+Reliable+Cross-Cloud+Kubernetes+Clusters+on+Spot+Instances+with+Drafter+and+PVM+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kGUN7aUBGTU
- YouTube title: Building Reliable Cross-Cloud Kubernetes Clusters on Spot Instances with Drafter and.. F. Pojtinger
- Match score: 1.015
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/building-reliable-cross-cloud-kubernetes-clusters-on-spot-instances-wi/kGUN7aUBGTU.txt
- Transcript chars: 41392
- Keywords: actually, running, snapshot, course, everything, migrate, little, usually, actual, second, migration, drafter, interesting, architect, instance, source, single, exactly

### Resumo baseado na transcript

all right well welcome everyone today's talk is about um building reliable cross Cloud kubernetes clusters on spot instances with drafter and pvm and I realized it's quite a mouthful it's quite a lot so we're going to take this step by step first of all we're going to start with commoditization that fundamental idea why you would want to do something like that and we're going to take a look at pvm which is an interesting C technology we're going to be using to start VMS inside of vmss

### Excerpt da transcript

all right well welcome everyone today's talk is about um building reliable cross Cloud kubernetes clusters on spot instances with drafter and pvm and I realized it's quite a mouthful it's quite a lot so we're going to take this step by step first of all we're going to start with commoditization that fundamental idea why you would want to do something like that and we're going to take a look at pvm which is an interesting C technology we're going to be using to start VMS inside of vmss without hardare acceleration support on them and without NE virualization support going to take a look at Silo a lopol apps project to migrate a lot of data between hosts very efficiently and you will take a look at drafter which is an open source project again baps that combines the two tools into a single framework then we will take a look at conduit which will take care of our Network migrations and finally we will take a look at architect which is the actual more or less product that you can use today so let's get started a little bit about myself I'm Felicitas you can find me on the fediverse if you interested and I of course work at lalabs mostly on drafter yeah let's get started first of all I want to talk to you about an actual quite interesting article on Cor of net called loss of tech commoditize your complement and the fundamental proposal of this article is that Smart Companies try to commoditize their products compliments now you might be wondering what exactly a complement refers to here and I think the best way to explain it is by giving you some examples for example if you have a car your your complement is usually electricity or gas without that you can't do much with it if you have if you put physical computers you need software to be your complement because without software your Hardware is just kind of a shiny piece of metal if you're Shipping Company you need a railroad or you need a road for for it to function so all of these companies usually require some other thing in order to function as their complement now this might seem a bit abstract in terms of tech at first but it's a pattern that shows over shows up over and over again because companies that produce cars want to make gas cheap companies that ship a lot of um one second companies to ship a lot of goods they want cheap transport they want rail to be available they want a road to be available and hard manufacturers want software to be cheap and commoditized so a very famous example of this commo
