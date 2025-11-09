import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set styling
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def create_language_analysis(df, output_path):
    """Create language analysis visualization"""
    print("Creating Language Analysis Visualization...")
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Count centres with language information
    centres_with_languages = df['languages'].notna().sum()
    french_programs = df['french_language_program'].notna().sum()
    indigenous_programs = df['indigenous_program'].notna().sum()
    
    # 1. Language program availability (Bar Chart)
    ax1 = axes[0]
    language_stats = {
        'Multiple Languages': centres_with_languages,
        'French Programs': french_programs,
        'Indigenous Programs': indigenous_programs
    }
    
    colors = ['#3498db', '#e74c3c', '#2ecc71']
    bars = ax1.bar(language_stats.keys(), language_stats.values(), 
                   color=colors, edgecolor='black', linewidth=1.5)
    ax1.set_ylabel('Number of Centres', fontsize=12, fontweight='bold')
    ax1.set_title('Language Program Availability', fontsize=14, fontweight='bold', pad=15)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # 2. Percentage breakdown (Pie Chart)
    ax2 = axes[1]
    total = len(df)
    percentages = {
        'Multilingual\nSupport': (centres_with_languages / total * 100),
        'French\nPrograms': (french_programs / total * 100),
        'Indigenous\nPrograms': (indigenous_programs / total * 100),
        'English\nOnly': ((total - centres_with_languages) / total * 100)
    }
    
    colors_pie = ['#3498db', '#e74c3c', '#2ecc71', '#95a5a6']
    wedges, texts, autotexts = ax2.pie(percentages.values(), 
                                         labels=percentages.keys(),
                                         autopct='%1.1f%%',
                                         startangle=90,
                                         colors=colors_pie,
                                         textprops={'fontsize': 10})
    
    # Make percentage text more visible
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(11)
    
    ax2.set_title('Language Service Distribution', fontsize=14, fontweight='bold', pad=15)
    
    plt.suptitle('EarlyON Child and Family Centres - Language Services Analysis', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Language analysis visualization saved to: {output_path}")
    
    # Print summary statistics
    print("\n" + "="*60)
    print("LANGUAGE SERVICES SUMMARY")
    print("="*60)
    print(f"Total Centres: {total}")
    print(f"Centres with Multiple Languages: {centres_with_languages} ({centres_with_languages/total*100:.1f}%)")
    print(f"Centres with French Programs: {french_programs} ({french_programs/total*100:.1f}%)")
    print(f"Centres with Indigenous Programs: {indigenous_programs} ({indigenous_programs/total*100:.1f}%)")
    print(f"English Only: {total - centres_with_languages} ({(total - centres_with_languages)/total*100:.1f}%)")
    print("="*60 + "\n")

def main():
    """Main function"""
    print("\n" + "="*60)
    print("EARLYON LANGUAGE ANALYSIS VISUALIZATION")
    print("="*60 + "\n")
    

    input_file = r"C:\Users\86185\Desktop\DSI\Assignments\visualization\02_activities\assignments\EarlyON_Child_and_Family_Centres_Locations_-_geometry_-_4326.csv"
    
    output_file = r"C:\Users\86185\Desktop\DSI\Assignments\visualization\02_activities\assignments\language_analysis.png"
    
    # Load data
    print(f"Loading data from: {input_file}")
    df = pd.read_csv(input_file)
    print(f"✓ Data loaded successfully! ({len(df)} centres)")
    
    # Create visualization
    create_language_analysis(df, output_file)
    
    print("\n✨ Visualization complete! ✨")
    print(f"Output saved to: {output_file}\n")

if __name__ == "__main__":
    main()