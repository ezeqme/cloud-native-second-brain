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
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Konstantinos Samaras-Tsakiris", "Rajula Vineet Reddy", "CERN"]
sched_url: https://kccnceu2021.sched.com/event/iE36/cerns-1500-drupal-websites-on-kubernetes-sailing-with-operators-konstantinos-samaras-tsakiris-rajula-vineet-reddy-cern
youtube_search_url: https://www.youtube.com/results?search_query=CERN%27s+1500+Drupal+Websites+on+Kubernetes%3A+Sailing+With+Operators+CNCF+KubeCon+2021
slides: []
status: parsed
---

# CERN's 1500 Drupal Websites on Kubernetes: Sailing With Operators - Konstantinos Samaras-Tsakiris & Rajula Vineet Reddy, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[101 Track]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Virtual / Virtual
- Speakers: Konstantinos Samaras-Tsakiris, Rajula Vineet Reddy, CERN
- Schedule: https://kccnceu2021.sched.com/event/iE36/cerns-1500-drupal-websites-on-kubernetes-sailing-with-operators-konstantinos-samaras-tsakiris-rajula-vineet-reddy-cern
- Busca YouTube: https://www.youtube.com/results?search_query=CERN%27s+1500+Drupal+Websites+on+Kubernetes%3A+Sailing+With+Operators+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre CERN's 1500 Drupal Websites on Kubernetes: Sailing With Operators.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE36/cerns-1500-drupal-websites-on-kubernetes-sailing-with-operators-konstantinos-samaras-tsakiris-rajula-vineet-reddy-cern
- YouTube search: https://www.youtube.com/results?search_query=CERN%27s+1500+Drupal+Websites+on+Kubernetes%3A+Sailing+With+Operators+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4O-pcSQR8Vw
- YouTube title: CERN's 1500 Drupal Websites on Kubernetes: Sa... Konstantinos Samaras-Tsakiris & Rajula Vineet Reddy
- Match score: 0.734
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cerns-1500-drupal-websites-on-kubernetes-sailing-with-operators/4O-pcSQR8Vw.txt
- Transcript chars: 17766
- Keywords: drupal, operator, operators, version, resource, actually, custom, running, upgrade, cluster, status, websites, serving, infrastructure, controller, essentially, change, exactly

### Resumo baseado na transcript

hello we are junior site reliability engineers from cern the world's largest particle physics laboratory i am constantinos and this is my colleague rajula and we would like to take you to sail with us today through our first experiences of building kubernetes operators this is cms one of the four big experiments at cern we try to understand nothing less than the origins of the universe at the heart of cms collisions happen many times per second between particles of two opposing particle beams and out of those collisions let's dive into the interesting part the demo so we'll try to upgrade through two of tuple sites live in the demo do note that we've been using the words update and upgrade interchangeably this is a mix of conventions of drupal and kubernetes but

### Excerpt da transcript

hello we are junior site reliability engineers from cern the world's largest particle physics laboratory i am constantinos and this is my colleague rajula and we would like to take you to sail with us today through our first experiences of building kubernetes operators this is cms one of the four big experiments at cern we try to understand nothing less than the origins of the universe at the heart of cms collisions happen many times per second between particles of two opposing particle beams and out of those collisions an explosion of secondary particles washes through the building-sized three-dimensional camera that is the particle detector and this produces a lot of data that then takes a complicated a large computing infrastructure to transform it into knowledge and that is a big part of certain engineers activities but because this is a big organization housing 12 000 and more physicists we want to take care of every aspect of their work and that includes public outreach so let's see what exactly we are going to talk about today first of all we want to explain to you what kind of infrastructure we are building it is related to public outreach how we use operators and what exactly they are then we want to show you upgrading some websites with with our operators and finally we'll see what we have learned so let's see what kind of infrastructure we are building this is home.cern our organization's homepage and it is housed on the infrastructure that we are replacing with this design together with about 1 000 and a bit more other websites all drupal websites made by a lot of people around the organization with different requirements and that every day hosts about 80 000 unique visitors and the peaks can reach even 1.5 times that much so drupal at cern is actually a rather complicated ecosystem we provide on top of core drupal a set of curated modules that are accessible to everyone but not everyone is a very wide-ranging set of users there's people that are that come from many backgrounds there's like physicists whose responsibilities also include site building and also administrative personnel and communications expert and actually a very small minority of the site administrators are actually web developers people with site building experience or drupal experts and all of these people need to have the same easy experience or very reliable hosting where they don't have to take a lot of responsibilities upon themselves to respond to security incidents or b
