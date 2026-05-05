---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Application + Delivery"
themes: ["Platform Engineering", "GitOps Delivery"]
speakers: ["Shahar Shmaram", "Ran Mansoor", "AppsFlyer"]
sched_url: https://kccnceu2023.sched.com/event/1Hyae/how-we-migrated-over-1000-services-to-backstage-using-gitops-and-survived-to-talk-about-it-shahar-shmaram-ran-mansoor-appsflyer
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Migrated+Over+1000+Services+to+Backstage+Using+GitOps+and+Survived+to+Talk+About+It%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# How We Migrated Over 1000 Services to Backstage Using GitOps and Survived to Talk About It! - Shahar Shmaram & Ran Mansoor, AppsFlyer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Application + Delivery]]
- Temas: [[Platform Engineering]], [[GitOps Delivery]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Shahar Shmaram, Ran Mansoor, AppsFlyer
- Schedule: https://kccnceu2023.sched.com/event/1Hyae/how-we-migrated-over-1000-services-to-backstage-using-gitops-and-survived-to-talk-about-it-shahar-shmaram-ran-mansoor-appsflyer
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Migrated+Over+1000+Services+to+Backstage+Using+GitOps+and+Survived+to+Talk+About+It%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre How We Migrated Over 1000 Services to Backstage Using GitOps and Survived to Talk About It!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyae/how-we-migrated-over-1000-services-to-backstage-using-gitops-and-survived-to-talk-about-it-shahar-shmaram-ran-mansoor-appsflyer
- YouTube search: https://www.youtube.com/results?search_query=How+We+Migrated+Over+1000+Services+to+Backstage+Using+GitOps+and+Survived+to+Talk+About+It%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2fCNqKxAtYo
- YouTube title: How We Migrated Over 1000 Services to Backstage Using GitOps and Survived to... - Shmaram & Mansoor
- Match score: 0.97
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/how-we-migrated-over-1000-services-to-backstage-using-gitops-and-survi/2fCNqKxAtYo.txt
- Transcript chars: 32954
- Keywords: backstage, solution, resources, developers, process, catalog, platform, within, github, githubs, resource, change, telephone, terraform, question, started, wanted, repository

### Resumo baseado na transcript

hi everyone and thank you for joining us it's a real pleasure to be here we have to say first that this is our first time as speakers so we are extremely nervous and when we saw the amount of people that register to our session which is approximately uh the amount of services that we were able to migrate we thought to ourselves maybe we should have migrated less um but we hope you're going to enjoy this session so this is a peanut butter peanut butter is a

### Excerpt da transcript

hi everyone and thank you for joining us it's a real pleasure to be here we have to say first that this is our first time as speakers so we are extremely nervous and when we saw the amount of people that register to our session which is approximately uh the amount of services that we were able to migrate we thought to ourselves maybe we should have migrated less um but we hope you're going to enjoy this session so this is a peanut butter peanut butter is a delicious spread it's made out of ground peanuts and it's full of protein right and this is jelly jelly is a sweet fruit-based spread that is full of vitamins now these two spreads are well known around the world right all of you probably know them kids love them and also adults but when you combine them both on a piece of bread you get the perfect sandwich which has the perfect combination twin sweet and salty now you're probably all wondering why are we talking about food right that's not for what we're here to talk about so we at app supplier did our own perfect sandwich by integrating these two well-known Technologies githubs on one hand and backstage on the other we were able to migrate all of our services and would like to tell you how we did it so hi everyone I'm Shaka next to me is run we both work in the platform team in apps flyer so if you're not familiar with apps player we are the market lead in Mobile distribution today you can see our amazing numbers above me we have around 14 000 customers around the world and we own 65 of the global market share today within apps player we have abstract engineering which has around 400 Engineers today which operate in autonomous squads these Engineers are responsible for over 1 000 microservices which are handling over 3 million events per second all these microservices are based on 200 and 250 000 Cloud resources now within the plot within the platform engineering we have the platform team platform team has around 50 Engineers which are divided into six groups and because we consider platform to be a product we also have product managers all these people together are responsible for assisting 350 r d engineers now it's important to know that we consider these Engineers to be our customers so we want to make sure that they can easily manage their resources let's see how we're able to evolve into the numbers you saw before so apps player was founded in 2011.

we started up as a small company we had a few developers and small amount of services that requir
