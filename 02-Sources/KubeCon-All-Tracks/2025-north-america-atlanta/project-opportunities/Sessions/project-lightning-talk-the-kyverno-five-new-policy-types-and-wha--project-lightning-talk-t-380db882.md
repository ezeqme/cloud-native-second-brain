---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["Security", "Community Governance"]
speakers: ["Cortney Nickerson", "Community Manager"]
sched_url: https://kccncna2025.sched.com/event/27d4W/project-lightning-talk-the-kyverno-five-new-policy-types-and-what-you-can-do-with-them-cortney-nickerson-community-manager
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+The+Kyverno+Five%3A+New+Policy+Types+And+What+You+Can+Do+With+Them+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: The Kyverno Five: New Policy Types And What You Can Do With Them - Cortney Nickerson, Community Manager

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Security]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Cortney Nickerson, Community Manager
- Schedule: https://kccncna2025.sched.com/event/27d4W/project-lightning-talk-the-kyverno-five-new-policy-types-and-what-you-can-do-with-them-cortney-nickerson-community-manager
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+The+Kyverno+Five%3A+New+Policy+Types+And+What+You+Can+Do+With+Them+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: The Kyverno Five: New Policy Types And What You Can Do With Them.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d4W/project-lightning-talk-the-kyverno-five-new-policy-types-and-what-you-can-do-with-them-cortney-nickerson-community-manager
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+The+Kyverno+Five%3A+New+Policy+Types+And+What+You+Can+Do+With+Them+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1WvHD-ihyfI
- YouTube title: Project Lightning Talk: The Kyverno Five: New Policy Types And What You Can Do... Cortney Nickerson
- Match score: 0.958
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-the-kyverno-five-new-policy-types-and-what-you/1WvHD-ihyfI.txt
- Transcript chars: 5181
- Keywords: policy, validating, everything, talking, resources, finally, everyone, policies, kyivero, expressions, performance, kyberno, without, function, resource, adopted, syntax, faster

### Resumo baseado na transcript

Uh and today we're going to be talking about our new common expression languagebased policy types. The lights are down, the crowd's buzzing, the stage is getting set for the headline act, which is the Kybero 5. So it's perfect because also K uh Kubernetes has adopted Cell and now we're all in sync playing the same uh sheet music and language. No performance is complete without somebody that goes around and keeps things cleaned up for the next time around and the next performance. So, you can query Kubernetes resources, validate image metadata, or run um regeneration uh and time timely operations in your direct cell uh expressions through our library mechanism. Uh you can see from the benchmarks here, everything gets exponentially better because we're all using Cell as is Kubernetes um to communicate with each other and so everything goes much faster.

### Excerpt da transcript

Hi everyone. I'm Courtney Nickerson. I'm going to be talking to you about Kyberno. It's your favorite um Kubernetes native policy engine. Uh and today we're going to be talking about our new common expression languagebased policy types. So first things first, imagine you're at a concert. The lights are down, the crowd's buzzing, the stage is getting set for the headline act, which is the Kybero 5. And those are our cellbased policies that we're going to be talking about today. So how does this work? Um first Kubernetes is our stage and record label. It sets the tempo. It schedules the gigs. It manages the lighting for everyone. Those are basically known to all of us as pods, nodes, and workloads. Without Kubernetes, Kyivero doesn't have a stage to actually function on. So we can't perform all of our duties. Um but the conductor is ensuring that every resource hits the right note. Now we're talking about our cell policies. Initially, Kyivero wrote its rules in YAML form. So, these were patterns. It was great for simple riffs like match this label or deny the deny that container.

Um, but as time has gone on, we want to jam out with very cool logic loops and other things. And so, we've now adopted Cell. Cell begins with a whole new sound for everyone. So, it has cleaner syntax that reads like code. It has compiled expressions for faster performance. Um, and it just generally has more range with logical operators and functions. So it's perfect because also K uh Kubernetes has adopted Cell and now we're all in sync playing the same uh sheet music and language. So let's meet the band very quickly. We've got validating policy uh our lead vocalists. We've got mutating policy on lead guitar. Generating policy on drums. Image validating policy is our band manager. And deleting policy is the crew behind the scenes that keeps everything clean. Um we'll go through very quickly. validating policy is going to be the voice of your cluster. It's going to extend Kubernetes validating admission policy. Very important for a lot of us um with Kyivero specific features like spec evaluation to decide which validations um need to be run at admission time in the background scan or an arbitrary JSON payloads for example.

So our cell expressions are inside your validations to enforce labels. Next we have mutating policy. It's going to add in different riffs. Uh it lets you modify requests using cell driven patches. So either apply configuration objects for declarative merges or JS
