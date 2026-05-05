---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Cloud Native Experience"
themes: ["Cloud Native Experience"]
speakers: ["Corey Quinn", "The Duckbill Group"]
sched_url: https://kccncna2025.sched.com/event/27FVz/the-myth-of-portability-why-your-cloud-native-app-is-married-to-your-provider-corey-quinn-the-duckbill-group
youtube_search_url: https://www.youtube.com/results?search_query=The+Myth+of+Portability%3A+Why+Your+Cloud+Native+App+Is+Married+To+Your+Provider+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Myth of Portability: Why Your Cloud Native App Is Married To Your Provider - Corey Quinn, The Duckbill Group

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[Cloud Native Experience]]
- País/cidade: United States / Atlanta
- Speakers: Corey Quinn, The Duckbill Group
- Schedule: https://kccncna2025.sched.com/event/27FVz/the-myth-of-portability-why-your-cloud-native-app-is-married-to-your-provider-corey-quinn-the-duckbill-group
- Busca YouTube: https://www.youtube.com/results?search_query=The+Myth+of+Portability%3A+Why+Your+Cloud+Native+App+Is+Married+To+Your+Provider+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Myth of Portability: Why Your Cloud Native App Is Married To Your Provider.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVz/the-myth-of-portability-why-your-cloud-native-app-is-married-to-your-provider-corey-quinn-the-duckbill-group
- YouTube search: https://www.youtube.com/results?search_query=The+Myth+of+Portability%3A+Why+Your+Cloud+Native+App+Is+Married+To+Your+Provider+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cvv1cVi1n9I
- YouTube title: The Myth of Portability: Why Your Cloud Native App Is Married To Your Provider - Corey Quinn
- Match score: 1.008
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-myth-of-portability-why-your-cloud-native-app-is-married-to-your-p/cvv1cVi1n9I.txt
- Transcript chars: 18133
- Keywords: clouds, disaster, portability, locked, center, provider, actually, talking, better, managed, shitty, either, native, bugout, preparing, vendor, specific, running

### Resumo baseado na transcript

Uh, preppers spend thousands of dollars on these things with freeze-dried food, water filtration, first aid kits, tactical gear, emergency radios, myar blankets, paracord, water purification tablets, and then they maintain this thing with a diligence none of us bring to our backups. They grab the bag, they grab the keys, and they're out the door in 90 seconds or less. And what that means is I see a lot of cloud architectures, good ones, bad ones, and ones that make me question the very nature of humanity. Kubernetes was supposed to solve this problem and abstract away all the cloud providers and machines underneath just like Java abstracted away Windows versus Linux versus Mac. Have you ever noticed how every startup with three users suddenly decides they need Kubernetes and off they go? It's because Kubernetes is a way for engineers who can't pass the technical interview at AWS, Google, or Azure to LAR as hypers scale cloud employees.

### Excerpt da transcript

All right, let's dive in then. Thank you all for coming. Bugout bags, a terrific way to start a talk. Uh, preppers spend thousands of dollars on these things with freeze-dried food, water filtration, first aid kits, tactical gear, emergency radios, myar blankets, paracord, water purification tablets, and then they maintain this thing with a diligence none of us bring to our backups. Uh, they obsessively focus on this. They rotate the food every six months. They check the batteries in this thing on a quarterly basis. They know exactly where the bag is in the closet by the front door. They have practiced the drill. They grab the bag, they grab the keys, and they're out the door in 90 seconds or less. They have planned the route, the primary route, the secondary route, the rally points, and they have thought through virtually every scenario. the grid goes down, economic collapse, uh, social unrest, nuclear winter, or here in Georgia, regular winter apparently, and then disaster actually strikes. The wildfire is coming over the ridge and what happens?

or the hurricane made landfall six hours early or the evacuation order came through and you know what they grab is their car keys, their phone, maybe the dog if they remember that far and they head out, leaving the bugout bag in the closet because in the actual moment of crisis, they don't have time for what they planned on. The disaster they prepared for is not the disaster that hit. They spent years and thousands of dollars preparing for a threat model that doesn't match their reality. Which brings me to cloud portability. I'm here to tell you that you have been preparing for the wrong disaster. For the last decade, a good part of the entire cloud native ecosystem has been selling you a story, usually of the form that cloud native is what we have to sell you. Uh it's a story about freedom. It's about portability. It's about never being locked in to a malicious vendor. It's about being able to switch clouds whenever the mood strikes you. Pick up your containers, you drop them into a new provider, and you're done.

That's the promise. So, today I'm going to show you why that's I am Corey Quinn. I help companies not get financially destroyed by their cloud bills. And what that means is I see a lot of cloud architectures, good ones, bad ones, and ones that make me question the very nature of humanity. So today we're talking about some of the bad patterns. Um, I should call this out because I will hear it on the in
