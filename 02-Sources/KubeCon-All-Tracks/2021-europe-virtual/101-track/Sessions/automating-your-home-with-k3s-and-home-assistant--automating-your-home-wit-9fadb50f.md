---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Eddie Zaneski", "Amazon Web Services", "Jeff Billimek", "The Home Depot"]
sched_url: https://kccnceu2021.sched.com/event/iE2B/automating-your-home-with-k3s-and-home-assistant-eddie-zaneski-amazon-web-services-jeff-billimek-the-home-depot
youtube_search_url: https://www.youtube.com/results?search_query=Automating+Your+Home+with+K3s+and+Home+Assistant+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Automating Your Home with K3s and Home Assistant - Eddie Zaneski, Amazon Web Services & Jeff Billimek, The Home Depot

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: Virtual / Virtual
- Speakers: Eddie Zaneski, Amazon Web Services, Jeff Billimek, The Home Depot
- Schedule: https://kccnceu2021.sched.com/event/iE2B/automating-your-home-with-k3s-and-home-assistant-eddie-zaneski-amazon-web-services-jeff-billimek-the-home-depot
- Busca YouTube: https://www.youtube.com/results?search_query=Automating+Your+Home+with+K3s+and+Home+Assistant+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Automating Your Home with K3s and Home Assistant.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2B/automating-your-home-with-k3s-and-home-assistant-eddie-zaneski-amazon-web-services-jeff-billimek-the-home-depot
- YouTube search: https://www.youtube.com/results?search_query=Automating+Your+Home+with+K3s+and+Home+Assistant+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=icyTnoonRqI
- YouTube title: Automating Your Home with K3s and Home Assistant - Eddie Zaneski & Jeff Billimek
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/automating-your-home-with-k3s-and-home-assistant/icyTnoonRqI.txt
- Transcript chars: 26782
- Keywords: assistant, running, basically, device, cluster, devices, z-wave, install, called, charts, version, automation, raspberry, actually, everything, automatically, together, connected

### Resumo baseado na transcript

hello and thank you for joining us my name is eddie zaneski and i serve as a developer advocate at amazon web services i'm also the co-chair of kubernetes 6 cli where i help maintain cube control i'm coming to you from denver colorado in the united states oh hi my name is jeff bilamek i'm a principal software engineer for the home depot i'm in atlanta georgia and i'm super happy to be here with you eddie we have one goal today and that's to inspire you to start

### Excerpt da transcript

hello and thank you for joining us my name is eddie zaneski and i serve as a developer advocate at amazon web services i'm also the co-chair of kubernetes 6 cli where i help maintain cube control i'm coming to you from denver colorado in the united states oh hi my name is jeff bilamek i'm a principal software engineer for the home depot i'm in atlanta georgia and i'm super happy to be here with you eddie we have one goal today and that's to inspire you to start a home lab when a lot of folks want to learn kubernetes or a lot of the cloud native technologies that are out there they don't really have a personal project to get started with it's much easier to throw yourself in and really learn all the things when you're actually managing something and so we don't obviously want you to run and play in your production environment if you can help it and so that's where uh the software we're going to show today really shines why don't we start off with talking about what what a home lab is so home labs can be very addicting just so you know before long you might find yourself looking for used servers on ebay late at night but but all seriousness home labs are a really safe way to experiment with new technologies either for your own personal use or maybe something related to your your job as for the why i think i think it really jumps into you know besides having fun outside of work it's a great place for you to improve your craft you know you can also get a whole bunch of practical applications and experience you know as you'll see with home automation the real question though is why would you want to run this inside of kubernetes for starters it's a really great way to learn kubernetes kubernetes provides really great features for like resiliency and redundancy like for example just the other day this week my power went out for about three hours the ups has all failed and so everything turned off and uh when the power finally came back on uh and everything powered back up kubernetes basically ensured that everything was running um without incident like everything just came back automatically thanks to the kubernetes scheduler and kubernetes just kind of gives you a place to put things maybe that one-off cron job that you have running that alerts you when there's a 90s dance party at the venue around your apartment like i used to once your cluster gets full you can always just you know grab another raspberry pi for example toss it in and grow it out one of the th
