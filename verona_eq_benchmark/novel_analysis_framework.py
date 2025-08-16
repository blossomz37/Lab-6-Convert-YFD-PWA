#!/usr/bin/env python3
"""
Novel Emotional Intelligence Analysis Framework
Adapted from EQBench3 to evaluate emotional intelligence in "Verona Resurrected"

This framework adapts EQBench3's emotional intelligence evaluation methods
to analyze the emotional depth, character development, and psychological
complexity in Carlo's Gothic reimagining of Romeo and Juliet.
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class NovelScenario:
    """Represents an emotional scenario extracted from the novel"""
    chapter: str
    scene_description: str
    characters_involved: List[str]
    emotional_themes: List[str]
    text_excerpt: str
    complexity_markers: List[str]

class NovelEQAnalyzer:
    """Analyzes emotional intelligence elements in Verona Resurrected"""
    
    def __init__(self, markdown_directory: str):
        self.markdown_dir = Path(markdown_directory)
        self.scenarios = []
        self.characters = {
            "The Apothecary": {
                "role": "Antagonist/Scientist",
                "emotional_arc": "Rationality vs Horror",
                "key_traits": ["scientific detachment", "hubris", "fear", "control"]
            },
            "Romeo": {
                "role": "Resurrected Lover", 
                "emotional_arc": "Corrupted Love",
                "key_traits": ["devotion", "supernatural bond", "violence", "protection"]
            },
            "Juliet": {
                "role": "Resurrected Lover",
                "emotional_arc": "Corrupted Love", 
                "key_traits": ["devotion", "supernatural bond", "defiance", "transformation"]
            },
            "Friar Lawrence": {
                "role": "Keeper of Ancient Knowledge",
                "emotional_arc": "Duty vs Compassion",
                "key_traits": ["wisdom", "burden", "faith", "sacrifice"]
            }
        }
        
    def extract_emotional_scenarios(self) -> List[NovelScenario]:
        """Extract key emotional intelligence scenarios from the novel"""
        scenarios = []
        
        # Define key emotional intelligence markers to look for
        eq_markers = {
            "empathy": ["understanding", "compassion", "feeling for", "sympathy"],
            "self_awareness": ["realized", "understood himself", "reflection", "introspection"], 
            "emotional_regulation": ["controlled", "restrained", "managed", "composed"],
            "social_awareness": ["sensed", "perceived", "noticed", "observed"],
            "relationship_management": ["influenced", "persuaded", "connected", "bonded"],
            "moral_reasoning": ["right", "wrong", "should", "ought", "duty", "responsibility"],
            "psychological_complexity": ["conflict", "torn", "struggled", "wavered"]
        }
        
        # Process each chapter
        for chapter_file in sorted(self.markdown_dir.glob("Chapter_*.md")):
            chapter_name = chapter_file.stem
            content = chapter_file.read_text(encoding='utf-8')
            
            # Extract key emotional scenes
            scenarios.extend(self._analyze_chapter_emotions(chapter_name, content, eq_markers))
            
        return scenarios
    
    def _analyze_chapter_emotions(self, chapter: str, content: str, eq_markers: Dict) -> List[NovelScenario]:
        """Analyze emotional intelligence elements in a specific chapter"""
        scenarios = []
        
        # Split content into paragraphs for analysis
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        
        for i, paragraph in enumerate(paragraphs):
            if len(paragraph) < 100:  # Skip very short paragraphs
                continue
                
            # Look for emotional intelligence markers
            detected_themes = []
            complexity_markers = []
            
            for eq_type, markers in eq_markers.items():
                for marker in markers:
                    if re.search(rf'\b{re.escape(marker)}\b', paragraph, re.IGNORECASE):
                        detected_themes.append(eq_type)
                        complexity_markers.append(marker)
            
            # If significant EQ content detected, create scenario
            if len(detected_themes) >= 2 or len(paragraph) > 500:
                characters_in_scene = self._identify_characters_in_text(paragraph)
                
                scenario = NovelScenario(
                    chapter=chapter,
                    scene_description=f"Emotional scene {i+1}",
                    characters_involved=characters_in_scene,
                    emotional_themes=list(set(detected_themes)),
                    text_excerpt=paragraph[:1000] + "..." if len(paragraph) > 1000 else paragraph,
                    complexity_markers=complexity_markers
                )
                scenarios.append(scenario)
        
        return scenarios
    
    def _identify_characters_in_text(self, text: str) -> List[str]:
        """Identify which characters appear in a given text passage"""
        characters_found = []
        character_names = {
            "Apothecary": ["Apothecary", "he", "his"],
            "Romeo": ["Romeo", "Montague boy"],
            "Juliet": ["Juliet", "Capulet girl"], 
            "Friar Lawrence": ["Friar Lawrence", "Friar", "Lawrence"],
            "Old Capulet": ["Old Capulet", "patriarch"],
            "Prince": ["Prince", "Escalus"]
        }
        
        for char_name, identifiers in character_names.items():
            for identifier in identifiers:
                if re.search(rf'\b{re.escape(identifier)}\b', text, re.IGNORECASE):
                    if char_name not in characters_found:
                        characters_found.append(char_name)
                    break
                    
        return characters_found
    
    def generate_eq_evaluation_prompts(self) -> List[Dict[str, Any]]:
        """Generate prompts for LLM evaluation of the novel's emotional intelligence"""
        prompts = []
        
        scenarios = self.extract_emotional_scenarios()
        
        for scenario in scenarios[:10]:  # Limit to top 10 most complex scenarios
            prompt = {
                "scenario_id": f"{scenario.chapter}_{scenario.scene_description}".replace(" ", "_"),
                "chapter": scenario.chapter,
                "evaluation_prompt": f"""
Please evaluate the emotional intelligence demonstrated in this passage from "Verona Resurrected":

**Context**: {scenario.chapter} - {scenario.scene_description}
**Characters**: {', '.join(scenario.characters_involved)}
**Detected Themes**: {', '.join(scenario.emotional_themes)}

**Text Passage**:
{scenario.text_excerpt}

**Evaluation Criteria**:
1. **Emotional Complexity** (0-20): How nuanced and sophisticated are the emotional dynamics?
2. **Character Psychology** (0-20): How well does the text reveal internal emotional states?
3. **Empathy & Understanding** (0-20): How well do characters understand each other's emotions?
4. **Moral Reasoning** (0-20): How sophisticated is the ethical/moral emotional reasoning?
5. **Literary Emotional Intelligence** (0-20): How effectively does the author convey complex emotions?

Please provide a score for each criterion and explain your reasoning. Total score out of 100.
                """,
                "characters_involved": scenario.characters_involved,
                "emotional_themes": scenario.emotional_themes,
                "text_excerpt": scenario.text_excerpt
            }
            prompts.append(prompt)
            
        return prompts
    
    def create_novel_benchmark_config(self) -> Dict[str, Any]:
        """Create a configuration for benchmarking the novel's emotional intelligence"""
        
        config = {
            "benchmark_name": "Verona Resurrected EQ Analysis",
            "novel_title": "Verona Resurrected", 
            "author": "Carlo",
            "analysis_date": datetime.now(timezone.utc).isoformat(),
            "methodology": "Adapted from EQBench3 for literary analysis",
            "evaluation_dimensions": [
                "Emotional Complexity",
                "Character Psychology", 
                "Empathy & Understanding",
                "Moral Reasoning",
                "Literary Emotional Intelligence"
            ],
            "characters_analyzed": list(self.characters.keys()),
            "total_chapters": len(list(self.markdown_dir.glob("Chapter_*.md"))),
            "scenarios_extracted": len(self.extract_emotional_scenarios()),
            "evaluation_prompts": self.generate_eq_evaluation_prompts()
        }
        
        return config

def main():
    """Main function to run novel EQ analysis"""
    markdown_dir = "/Users/carlo/Documentation_Your_First_Draft/lab_6_markdown_conversion_project/markdown_yfd"
    
    analyzer = NovelEQAnalyzer(markdown_dir)
    
    print("🧠 Novel Emotional Intelligence Analysis Framework")
    print("=" * 50)
    
    # Extract scenarios
    scenarios = analyzer.extract_emotional_scenarios()
    print(f"📚 Extracted {len(scenarios)} emotional scenarios from novel")
    
    # Generate evaluation config
    config = analyzer.create_novel_benchmark_config()
    
    # Save configuration
    config_file = Path("verona_resurrected_eq_config.json")
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"📝 Saved benchmark configuration to {config_file}")
    print(f"🎭 Characters analyzed: {', '.join(config['characters_analyzed'])}")
    print(f"📊 Evaluation prompts generated: {len(config['evaluation_prompts'])}")
    
    # Show sample scenario
    if scenarios:
        sample = scenarios[0]
        print(f"\n📖 Sample Emotional Scenario:")
        print(f"Chapter: {sample.chapter}")
        print(f"Themes: {', '.join(sample.emotional_themes)}")
        print(f"Characters: {', '.join(sample.characters_involved)}")
        print(f"Text preview: {sample.text_excerpt[:200]}...")

if __name__ == "__main__":
    main()
